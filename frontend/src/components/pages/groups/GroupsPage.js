import React, { useEffect, useState } from "react";

import Asset from "../../../components/Asset.js"

import Container from "react-bootstrap/esm/Container";
import Card from "react-bootstrap/Card";
import Col from "react-bootstrap/esm/Col";
import Row from "react-bootstrap/esm/Row";
import Button from "react-bootstrap/Button";
import { Link } from "react-router-dom";

import styles from "../../../styles/GroupsPage.module.css";
import appStyles from "../../../App.module.css";
import btnStyles from "../../../styles/Button.module.css";
import NoResults from "../../../assets/no-results.png";

import { useLocation } from "react-router-dom";
import { axiosReq } from "../../../api/axiosDefaults";


function GroupsPage(message, filter = "" ) {
  const [groups, setGroups] = useState({ results: [] }); 
  const [hasLoaded, setHasLoaded] = useState(false);
  const { pathname } = useLocation();


  useEffect(() => {
    const fetchGroups = async () => {
      try {
        const { data } = await axiosReq.get(`/groups/?${filter}`);
        setGroups(data);
        console.log(data)
        setHasLoaded(true);
      } catch (err) {
        console.log(err);
      }
    };

    setHasLoaded(false);
    fetchGroups();
  }, [filter, pathname]);

  return (
    <Container>
      <h1>Groups</h1>
      <Row>
        {hasLoaded ? (
          <>
            {groups.results.length ? (
              groups.results.map((group) => (
                <Col md={4} >
                  <Card className={`${appStyles.Content} ${styles.Card} mb-4`}>
                    <i className="fa-solid fa-bahai text-center mt-4"></i>
                    <Card.Body className="text-center">
                      <Card.Title>{group.name}</Card.Title>
                        <Card.Text>
                            Group members nr-- to fix
                        </Card.Text>
                        <Button as={Link} className={btnStyles.Button}>View Group</Button>
                    </Card.Body>
                    <Card.Footer className={styles.Footer}>{group.created_at} - {group.created_by}</Card.Footer>
                  </Card>
                </Col>
              ))
              ) : (
                <Container className={appStyles.Content}>
                  <Asset src={NoResults} message={message} />
                </Container>
            )}
          </>
        ) : (
          <Container className={appStyles.Content}>
            <Asset spinner />
          </Container>
        )}
      </Row>
    </Container>
  )
};

export default GroupsPage;
