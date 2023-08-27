import React, {useState} from "react";
import { Link } from "react-router-dom";

import styles from "../../../styles/SignInUpForm.module.css";
import btnStyles from "../../../styles/Button.module.css";
import appStyles from "../../../../src/App.module.css";

import Form from "react-bootstrap/Form";
import Alert from "react-bootstrap/Alert";
import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Container from "react-bootstrap/Container";

import axios from "axios";
import { useHistory } from "react-router-dom";

const SignUpForm = () => {
    const [signUpData, setSignUpData] = useState({
        username: "",
        password1: "",
        password2: "",
    });
    const {username, password1, password2} = signUpData;
    const history = useHistory();

    const [errors, setErrors] = useState({});

    const handleChange = (event) => {
        setSignUpData({
          ...signUpData,
          [event.target.name]: event.target.value,
        });
    };
    
    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
          await axios.post("/dj-rest-auth/registration/", signUpData);
          history.push("/signin");
        } catch (err) {
          setErrors(err.response?.data);
        }
    };

    return (
        
        <Row className={styles.Row}>
            <Col className="my-auto py-2 p-md-2" md={6}>
            <h1 className="text-center">Signup here:</h1>
                <Container className={`${appStyles.Content} p-4 `}>

                    <Form onSubmit={handleSubmit}>
                        <Form.Group controlId="username">
                            <Form.Label className="d-none">Username</Form.Label>
                            <Form.Control 
                                className={styles.Input}
                                type="text" 
                                placeholder="Choose a username"
                                name="username" 
                                value={username}
                                onChange={handleChange}
                            />
                        </Form.Group>
                        {errors.username?.map((message, idx) => (
                            <Alert variant="warning" key={idx}>
                                {message}
                            </Alert>
                        ))}

                        <Form.Group controlId="password1">
                            <Form.Label className="d-none">Password</Form.Label>
                            <Form.Control 
                                className={styles.Input}
                                type="password" 
                                placeholder="Choose a password"
                                name="password1" 
                                value={password1}
                                onChange={handleChange}
                            />
                        </Form.Group>
                        {errors.password1?.map((message, idx) => (
                            <Alert key={idx} variant="warning">
                                {message}
                            </Alert>
                        ))}

                        <Form.Group controlId="password2">
                            <Form.Label className="d-none">Password</Form.Label>
                            <Form.Control 
                                className={styles.Input}
                                type="password" 
                                placeholder="Confirm your password"
                                name="password2"
                                value={password2}
                                onChange={handleChange}
                            />
                        </Form.Group>
                        {errors.password2?.map((message, idx) => (
                            <Alert key={idx} variant="warning">
                                {message}
                            </Alert>
                        ))}

                        <Button 
                            className={`${btnStyles.Button} ${btnStyles.Wide}`} 
                            type="submit"
                        >
                            Sign up
                        </Button>
                        {errors.non_field_errors?.map((message, idx) => (
                            <Alert key={idx} variant="warning" className="mt-3">
                                {message}
                            </Alert>
                        ))}
                    </Form>

                </Container>
                <Container className={`mt-3 ${appStyles.Content}`}>
                    <Link className={styles.Link} to="/signin">
                        Already have an account? <span>Sign in</span>
                    </Link>
                </Container>
            </Col>
        </Row>
    );
};

export default SignUpForm;