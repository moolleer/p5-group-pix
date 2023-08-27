import React, {useState} from "react";

import Form from "react-bootstrap/Form";
import Alert from "react-bootstrap/Alert";
import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Container from "react-bootstrap/Container";

import { Link } from "react-router-dom";

import styles from "../../../styles/SignInUpForm.module.css";
import btnStyles from "../../../styles/Button.module.css";
import appStyles from "../../../App.module.css";

import axios from "axios";
import { useHistory } from "react-router-dom";
import { useSetCurrentUser } from "../../../contexts/CurrentUserContext";


function SignInForm() {
    const setCurrentUser = useSetCurrentUser();

    const [signInData, setSignInData] = useState({
        username: "",
        password1: "",
    });
    const {username, password} = signInData;
    const history = useHistory();

    const [errors, setErrors] = useState({});

    const handleChange = (event) => {
        setSignInData({
          ...signInData,
          [event.target.name]: event.target.value,
        });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
          const {data} = await axios.post("/dj-rest-auth/login/", signInData);
          setCurrentUser(data.user)
          history.push("/");
        } catch (err) {
          setErrors(err.response?.data);
        }
    };

    return (
        <Row className={styles.Row}>
            <Col className="my-auto py-1 p-md-2" md={6}>
            <h1 className="text-center">Sign in:</h1>
                <Container className={`${appStyles.Content} p-4 `}>
          
                    <Form onSubmit={handleSubmit}>
                        <Form.Group controlId="username">
                        <Form.Label className="d-none">Username</Form.Label>
                            <Form.Control 
                                className={styles.Input}
                                type="text" 
                                placeholder="Username"
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

                        <Form.Group controlId="password">
                        <Form.Label className="d-none">Password</Form.Label>
                            <Form.Control 
                                className={styles.Input}
                                type="password" 
                                placeholder="Password"
                                name="password" 
                                value={password}
                                onChange={handleChange}
                            />
                        </Form.Group>
                        {errors.password?.map((message, idx) => (
                            <Alert key={idx} variant="warning">
                                {message}
                            </Alert>
                        ))}

                        <Button 
                            className={`${btnStyles.Button} ${btnStyles.Wide}`} 
                            type="submit"
                        >
                            Sign in
                        </Button>
                        {errors.non_field_errors?.map((message, idx) => (
                            <Alert key={idx} variant="warning" className="mt-3">
                                {message}
                            </Alert>
                        ))}
                    </Form>
          
                </Container>
                <Container className={`mt-3 ${appStyles.Content}`}>
                    <Link className={styles.Link} to="/signup">
                        Don't have an account? <span>Sign up now!</span>
                    </Link>
                </Container>
            </Col>
        </Row>
    );
}

export default SignInForm;