
import React, {useEffect, useState} from 'react'
import logo from './logo.svg';
import './App.css';




const loadTweets = function(callback){
  const xhr = new XMLHttpRequest()
  const method = 'GET'
  const url = 'http://localhost:8000/api/tweets'
  const responseType = 'json'
  xhr.responseType = responseType
  xhr.open(method, url)
  xhr.onload = function(){
    callback(xhr.response, xhr.status)
    console.log(url)

}
xhr.onerror = function(e){
  console.log(e)
  callback({'message':'The request was an error'})
}

xhr.send()
}


function ActionBtn(props){
  const {tweet} = props
  const className = props.className ? props.className : 'btn btn-primary'
  return <button className={className}>{ tweet.likes }Likes</button>
}

function Tweet(props) {
  const{tweet} = props
  const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
  return <div className={className}>
       <p>{tweet.content} - {tweet.id}</p>
       <div className='btn btn-group' >
        <ActionBtn tweet={tweet} />
       </div>
    </div>




}

function App() {

  const [tweets, setTweets] = useState([])

  useEffect(()=>{
    const myCallback = (response, status) =>{
      if (status === 200){
        setTweets(response)
      } else {
        alert("There was an error")
      }
      
    }
    loadTweets(myCallback)
    // Do my look up

  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
        {tweets.map(( item, index) =>{
          return <Tweet tweet={item} className='my-5 py-5 border bg-white text-black text-dark' key={`${index}-{item.id}`}/>
        })}
        </div>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
