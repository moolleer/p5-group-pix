import styles from './App.module.css'
import NavBar from './components/NavBar';
import Container  from 'react-bootstrap/Container';
import { Route, Switch } from "react-router-dom";
import './api/axiosDefaults'
import SignUpForm from './components/pages/auth/SignUpForm';
import SignInForm from './components/pages/auth/SignInForm';
import GroupsCreateForm from './components/pages/groups/GroupsCreateForm';
import GroupsPage from './components/pages/groups/GroupsPage';
import MyGroupsPage from './components/pages/groups/MyGroupsPage';
import { useCurrentUser } from './contexts/CurrentUserContext';


function App() {
  const currentUser = useCurrentUser();
  const profile_id = currentUser?.profile_id || "";
  
  return (
      <div className={styles.App}>
        <NavBar />
        <Container className={styles.Main}>
          <Switch>
            <Route exact path="/" render={() => <h1>Home page</h1>} />
            <Route exact path="/signin" render={() => <SignInForm />} />
            <Route exact path="/signup" render={() => <SignUpForm />} />
            <Route exact path="/groups/create" render={() => <GroupsCreateForm />} />
            <Route 
              exact 
              path="/groups" 
              render={() => (
                <GroupsPage 
                message="No results found. Adjust the search keyword!" /> 
              )}
            />
            <Route 
              exact 
              path="/my-groups" 
              render={() => (
                <MyGroupsPage  
                filter={`created_by__profile=${profile_id}&`}
                />
              )}
            />
            <Route render={() => <p>Page not found!</p>} />
          </Switch>
        </Container>
      </div>
  );
}

export default App;