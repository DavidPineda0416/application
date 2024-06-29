import { useState, useRef } from "react";
import TodoList from "./TodoList";

//フックス　//プロップス
function App() {
  const [todos, setTodos] = useState([
    {id: 1, name: "Todo1" , complated: false},
  ]);
  const todoNmaeRef = useRef();


  //タスクを追加する
  const handleAddTodo = () =>{
    const name = todoNmaeRef.current.value;
    if(name === "")return; //空白の場合の処理のストップ
    setTodos((prevTodos) => {
      return[...prevTodos, {id: 1, name: name , complated: false}];
    });
    todoNmaeRef.current.value = null;
  };


  //一致するIDを見つけてくる
  const toggleTodo = (id) =>{
    const newTodos = {...todos};
    const todo = newTodos.find((todo) => todo.id === id);
    todo.complated = !todo.complated;
    setTodos(newTodos);
  };


//残りのタスクを表示
  const handleClear = () =>{
    const newTodos = todos.filter((todo) => !todo.complated );
    setTodos(newTodos);
  };


  //表示画面
  return( 
    <>
      <TodoList  todos = {todos} toggleTodo = {toggleTodo}/>
      <input type="text" ref={todoNmaeRef}/>
      <button onClick={handleAddTodo}>タスク追加</button>
      <button onClick={handleClear}>完了したタスクの削除</button>
      <div>残りのタスク:{todos.filter((todo) => !todo.complated).length}</div>
    </>
    ); 
  }

export default App;
