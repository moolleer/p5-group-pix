import React from 'react'
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";

import logo from "../assets/logo.png"
import styles from "../styles/NavBar.module.css"
import { NavLink } from "react-router-dom";
import { useCurrentUser, useSetCurrentUser } from '../contexts/CurrentUserContext';
import Avatar from "./Avatar";
import axios from "axios";

/**
 * Navbar component to render all navigationlinks
 */
const NavBar = () => {
  const currentUser = useCurrentUser();
  const setCurrentUser = useSetCurrentUser();

  const handleSignOut = async () => {
    try {
      await axios.post("dj-rest-auth/logout/");
      setCurrentUser(null);
    } catch (err) {
      console.log(err);
    }
  };

  const loggedInProfile = (
    <>
      <NavLink
        className={styles.NavLink}
        to={`/profiles/${currentUser?.profile_id}`}
      >
        <Avatar src={currentUser?.profile_picture} height={40} />
        {currentUser?.username}
      </NavLink>
    </>
  );

  const loggedIn = (
    <>
      <NavLink 
        to="/groups/" 
        className={styles.NavLink} 
        activeClassName={styles.Active}
      >
        View Groups
      </NavLink>
      <NavLink 
        to="/groupmemberships/" 
        className={styles.NavLink} 
        activeClassName={styles.Active}
      >
        My Groups
      </NavLink>
      <NavLink 
        to="/" 
        onClick={handleSignOut}
        className={styles.NavLink} 
      >
        Sign out
      </NavLink>
    </>
  );
    
  const loggedOut = (
    <>
      <NavLink 
        to="/signin" 
        className={styles.NavLink} 
        activeClassName={styles.Active}
      >
        Sign in
      </NavLink>
      <NavLink 
        to="/signup" 
        className={styles.NavLink} 
        activeClassName={styles.Active}
      >
        Sign up
      </NavLink>
    </>
  );

  return (
    <Navbar expand="md" fixed="sticky-top" className={styles.CustomNavbar} >
      <Container>
        <Navbar.Brand>
          <img className={styles.Round} src={logo} alt="logo" height="120" />
        </Navbar.Brand>
        {currentUser && loggedInProfile}
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

            {currentUser ? loggedIn : loggedOut}

          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar