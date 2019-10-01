import React, { Component } from 'react';
import './App.css';
import Person from './Person/Person';
import Hello from './Person/Hello'

    

class App extends Component {
  state = {
    persons : [
              {name : 'shinu', age : 18},
              {name : 'munni', age : 19},
              {name : 'sundi', age : 20}
          ]
  };
  switchNameHandler = () => {
    console.log("This is clicked!");
  }

  render() {
    return (
      <div className="App">
          <h1>Hi I'am A React App</h1>
          <button onClick={this.switchNameHandler}>Switch Name</button>
          <Person name={this.state.persons[0].name} age={this.state.persons[0].age}/>
          <Person name={this.state.persons[1].name} age={this.state.persons[1].age}/>
          <Person name={this.state.persons[2].name} age={this.state.persons[2].age}/>
      </div>
    );
  }
}

export default App;
