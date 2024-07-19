'use client'
import React, { useState, useEffect } from 'react'

export default function Home() {
  const [message, setMessage] = useState('Loading')

useEffect(() => {
  fetch('/api/hello')
    .then((res) => res.json())
    .then((data) => setMessage(data.message))
} , [])

  return (
    <div>
      <h1>{message}</h1>
    </div>
  )
}

