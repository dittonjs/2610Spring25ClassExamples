import { useState } from "react"

export function Input({label, ...props}) {


  return (
    <label className="input-label">
      {label}
      <input
        className="input"
        onChange={(e) => setValue(e.target.value)}
        {...props}
      />
    </label>
  )
}
