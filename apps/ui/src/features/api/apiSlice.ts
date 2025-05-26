import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export interface Post {
  id: number
  title: string
}

export const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
  endpoints: builder => ({
    getPosts: builder.query<Post[], void>({
      query: () => '/posts',
      // stubbed data
      transformResponse: () => [
        { id: 1, title: 'First post' },
        { id: 2, title: 'Second post' },
      ],
    }),
  }),
})

export const { useGetPostsQuery } = api
