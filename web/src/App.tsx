import { useQuery, gql } from "@apollo/client";

const HELLO_WORLD = gql`
  query {
    users {
      username
      createdAt
      isSuperuser
      uid
    }
  }
`;

function App() {
  const { loading, error, data } = useQuery(HELLO_WORLD);
  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return (
    <>
      <div className="container bg-slate-400">
        <h1 className="text-4xl font-bold text-center text-white">
          Welcome to RedwoodJS
        </h1>
        <div className="flex justify-center mt-8">
          <div className="text-center">
            <h2 className="text-2xl font-bold">Users</h2>
            <ul>
              {data.users.map((user: any) => (
                <li key={user.uid}>
                  {user.username} - {user.isSuperuser ? "Admin" : "User"}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
