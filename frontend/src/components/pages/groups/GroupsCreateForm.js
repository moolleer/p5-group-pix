import React, { useState } from 'react'
import Form from "react-bootstrap/Form";
import Alert from "react-bootstrap/Alert";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";

import styles from "../../../styles/GroupCreateForm.module.css";
import appStyles from "../../../App.module.css";
import btnStyles from "../../../styles/Button.module.css";
import { useHistory } from 'react-router-dom';
import { axiosReq } from '../../../api/axiosDefaults';


function GroupsCreateForm() {
    const [errors, setErrors] = useState({});
    
    const [postData, setPostData] = useState({
        name: "",
        description: "",
    });
    const { name, description } = postData;

    const history = useHistory();

    const handleChange = (event) => {
        setPostData({
          ...postData,
          [event.target.name]: event.target.value,
        });
      };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
    
        formData.append("name", name);
        formData.append("description", description);
    
        try {
          const { data } = await axiosReq.post("/groups/", formData);
          history.push(`/groups/${data.id}`);
          console.log(data)
        } catch (err) {
          console.log(err);
          if (err.response?.status !== 401) {
            console.log("Error Response Data:", err.response?.data);
            setErrors(err.response?.data);
            
          }
        }
      };
    

    return (
        <Row className={styles.Row}>
            <Col className="my-auto py-2 p-md-2" md={6}>
                <h1 className="text-center">Create Your Group Here:</h1>
                    <Container className={`${appStyles.Content} p-4 `}>

                        <Form onSubmit={handleSubmit}>
                            <Form.Group controlId="name">
                                <Form.Label>Group Name</Form.Label>
                                <Form.Control 
                                    className={styles.Input}
                                    type="text" 
                                    name="name" 
                                    value={name}
                                    onChange={handleChange}
                                />
                            </Form.Group>
                            {errors.name?.map((message, idx) => (
                                <Alert variant="warning" key={idx}>
                                    {message}
                                </Alert>
                            ))}

                            <Form.Group controlId="description">
                                <Form.Label>Describe Your Group:</Form.Label>
                                <Form.Control 
                                    as="textarea"
                                    rows={8} 
                                    name="description" 
                                    value={description}
                                    onChange={handleChange}
                                />
                            </Form.Group>
                            {errors.description?.map((message, idx) => (
                                <Alert key={idx} variant="warning">
                                    {message}
                                </Alert>
                            ))}

                            <Button 
                                className={`${btnStyles.Button} ${btnStyles.Wide}`} 
                                type="submit"
                            >
                                Create Group
                            </Button>
                            {errors.non_field_errors?.map((message, idx) => (
                                <Alert key={idx} variant="warning" className="mt-3">
                                    {message}
                                </Alert>
                            ))}
                        </Form>
                    </Container>
            </Col>
        </Row>
    );
};

export default GroupsCreateForm