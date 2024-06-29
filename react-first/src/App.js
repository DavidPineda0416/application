import TodoList from "./TodoList";


function App() {
  return( 
    <>
      <TodoList />
      <input type="text"/>
      <button>タスク追加</button>
      <button>完了したタスク</button>
      <div>残りのタスク</div>
    </>
    ); 
  }

export default App;
