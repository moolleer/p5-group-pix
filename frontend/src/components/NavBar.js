import React from 'react'
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";

import logo from "../assets/logo.png"
import styles from "../styles/NavBar.module.css"
import { NavLink } from "react-router-dom";


const NavBar = () => {
  return (
    <Navbar expand="md" fixed="sticky-top" className={styles.CustomNavbar} >
      <Container>
        <Navbar.Brand>
          <img className={styles.Round} src={logo} alt="logo" height="120" />
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ml-auto text-center">
            <NavLink 
              exact
              to="/" 
              className={styles.NavLink} 
              activeClassName={styles.Active} 
            >
              Home
            </NavLink >
            <NavLink to="/signin" className={styles.NavLink} activeClassName={styles.Active}>
              Sign in
            </NavLink>
            <NavLink to="/signup" className={styles.NavLink} activeClassName={styles.Active}>
              Sign up
            </NavLink>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar