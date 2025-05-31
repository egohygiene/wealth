import type { User } from './user'

export interface Message {
  id: number
  message: string
  user: User
  created_at: string
  updated_at: string
}
