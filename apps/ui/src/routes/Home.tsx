import { useGetFinanceSummaryQuery } from '../features/api/apiSlice'
import Chart from '../components/Chart'
import AuthStatus from '../components/AuthStatus'
import Messages from '../components/Messages'

export default function Home() {
  const { data, isLoading, isError, error } = useGetFinanceSummaryQuery()
  return (
    <div className="p-4">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Home</h1>
        <AuthStatus />
      </div>
      {isLoading && 'Loading...'}
      {isError && <div className="text-red-500">Error: {String(error)}</div>}
      {!isLoading && !isError && (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      )}
      <Chart />
      <Messages />
    </div>
  )
}
