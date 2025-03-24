export function RoundedButton({ onClick, children }) {
  return (
    <button className="rounded-button uppercase" onClick={onClick}>{children}</button>
  )
}
