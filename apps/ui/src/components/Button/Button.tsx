import type { ButtonProps } from './Button.types'

export default function Button({ label, ...props }: ButtonProps) {
  return (
    <button className="px-4 py-2 bg-blue-600 text-white rounded" {...props}>
      {label}
    </button>
  )
}
