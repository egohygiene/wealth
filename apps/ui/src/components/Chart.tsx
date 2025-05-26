import { useEffect, useRef } from 'react'
import { VisXYContainer, VisLine, VisAxis } from 'unovis'

export default function Chart() {
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!ref.current) return
    const container = new VisXYContainer(ref.current, {
      components: [
        new VisLine({ x: d => d.x, y: d => d.y }),
        new VisAxis('x'),
        new VisAxis('y'),
      ],
    })
    container.data = [{ x: 0, y: 0 }, { x: 1, y: 1 }]
    return () => container.destroy()
  }, [])

  return <div ref={ref} className="w-full h-40" />
}
