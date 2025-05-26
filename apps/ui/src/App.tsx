import { Link, Route, Routes } from 'react-router-dom'
import { useGetPostsQuery } from './features/api/apiSlice'
import Chart from './components/Chart'

function Home() {
  const { data, isLoading } = useGetPostsQuery()
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Home</h1>
      {isLoading ? 'Loading...' : <pre>{JSON.stringify(data, null, 2)}</pre>}
      <Chart />
    </div>
  )
}

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="*" element={<div>Not Found</div>} />
    </Routes>
  )
}
