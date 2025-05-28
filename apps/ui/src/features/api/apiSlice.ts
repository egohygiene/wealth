import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import type { Finance, FinanceSummary } from '../../types/models'
import { API_BASE_URL } from '../../config'

export interface Post {
  id: number
  title: string
}

export const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({ baseUrl: API_BASE_URL }),
  endpoints: builder => ({
    getPosts: builder.query<Post[], void>({
      query: () => '/posts',
      // stubbed data
      transformResponse: () => [
        { id: 1, title: 'First post' },
        { id: 2, title: 'Second post' },
      ],
    }),
    getFinance: builder.query<Finance, void>({
      query: () => '/finance',
      // stubbed data to illustrate typing
      transformResponse: (): Finance => ({
        user_id: 'demo',
        allocations: [],
        expenses: [],
        income_streams: [],
        debts: [],
        investments: [],
        portfolios: [],
        services: [],
        roles: [],
        features: [],
        lifecycle_phase: 'stabilizing',
        risk_profile: 'balanced',
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
      }),
    }),
    getFinanceSummary: builder.query<FinanceSummary, void>({
      query: () => '/finance/summary',
      transformResponse: (): FinanceSummary => ({
        net_worth: 0,
        investment_count: 0,
        debt_count: 0,
        allocation_count: 0,
      }),
    }),
  }),
})

export const { useGetPostsQuery, useGetFinanceQuery, useGetFinanceSummaryQuery } = api
