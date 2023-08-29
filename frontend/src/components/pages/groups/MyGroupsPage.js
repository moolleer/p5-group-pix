import React from 'react'
import { NavLink } from "react-router-dom";

import styles from "../../../styles/MyGroupsPage.module.css";

function MyGroupsPage() {
  return (
    <div>
      <h1>My Groups</h1> 
      <span className={styles.Add}>
        <NavLink to="/groups/create">
          {" "}
          <i class="fa-solid fa-square-plus"></i>Create a Group
      </NavLink>
      </span>
    </div>
  )
}

export default MyGroupsPage