import React from 'react'
import { NavLink } from 'react-router-dom';
import { useCurrentUser } from '../../../contexts/CurrentUserContext';
import Container from 'react-bootstrap/esm/Container';



function GroupsPage() {
    const currentUser = useCurrentUser();
    console.log(currentUser)

  return (
    <Container>
      <h1>Groups</h1>
        
          <NavLink to="/groups/create" > <i className="far fa-plus-square"></i>Add Group</NavLink>
        
      
    </Container>
    

  );
};

export default GroupsPage