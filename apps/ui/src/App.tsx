import { Route, Routes } from 'react-router-dom'
import { useGetFinanceSummaryQuery } from './features/api/apiSlice'
import Chart from './components/Chart'
import AuthStatus from './components/AuthStatus'

function Home() {
  const { data, isLoading } = useGetFinanceSummaryQuery()
  return (
    <div className="p-4">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Home</h1>
        <AuthStatus />
      </div>
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
