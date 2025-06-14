import { render, screen } from '@testing-library/react'
import { Button } from './'

describe('Button', () => {
  it('renders label', () => {
    render(<Button label="Test" />)
    expect(screen.getByText('Test')).toBeInTheDocument()
  })
})
