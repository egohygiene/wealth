import { useState } from 'react'
import { useAuth } from 'react-oidc-context'
import {
  useCreateMessageMutation,
  useGetMessagesQuery,
} from '../features/api/apiSlice'

export default function Messages() {
  const auth = useAuth()
  const { data: messages = [] } = useGetMessagesQuery()
  const [createMessage] = useCreateMessageMutation()
  const [text, setText] = useState('')

  if (!auth.isAuthenticated) {
    return <p>Please login to send messages.</p>
  }

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!text) return
    await createMessage(text).unwrap()
    setText('')
  }

  return (
    <div className="space-y-2">
      <form onSubmit={onSubmit} className="flex gap-2">
        <input
          value={text}
          onChange={e => setText(e.target.value)}
          className="border px-2 py-1 flex-1"
        />
        <button className="px-3 py-1 bg-gray-200 rounded" type="submit">
          Send
        </button>
      </form>
      <ul className="space-y-1">
        {messages.map(m => (
          <li key={m.id} className="border p-2 rounded">
            <strong>{m.user.preferred_username || m.user.sub}:</strong>{' '}
            {m.message}
          </li>
        ))}
      </ul>
    </div>
  )
}
