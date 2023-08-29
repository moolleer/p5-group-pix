import React, { useState } from "react";
import { NavLink } from "react-router-dom";

import Container from "react-bootstrap/esm/Container";
import Card from "react-bootstrap/Card";
import Col from "react-bootstrap/esm/Col";
import Row from "react-bootstrap/esm/Row";
import Button from "react-bootstrap/Button";
import { Link } from "react-router-dom";

import styles from "../../../styles/GroupsPage.module.css";
import appStyles from "../../../App.module.css";
import btnStyles from "../../../styles/Button.module.css";

function GroupsPage(message) {
  const [groups, setGroups] = useState({ results: [] }); 
  const [hasLoaded, setHasLoaded] = useState(false);
  





  return (
    <Container>
      <h1>Groups</h1>
      <NavLink to="/groups/create">
        {" "}
        <i className="far fa-plus-square"></i>Create a Group
      </NavLink>
      <Row>
        <Col md={4} >
          <Card className={`${appStyles.Content} mb-4`}>
            <i className="fa-solid fa-bahai text-center mt-4"></i>
            <Card.Body className="text-center">
              <Card.Title>Group Name</Card.Title>
              <Card.Text>
                Group members nr
                </Card.Text>
              <Button as={Link} className={btnStyles.Button}>View Group</Button>
            </Card.Body>
            <Card.Footer className={styles.Footer}>Created at - created by</Card.Footer>
          </Card>
        </Col>
      </Row>
    </Container>
  )
};

export default GroupsPage;
