'use client'
import { useState } from 'react'
import { useRouter } from 'next/navigation'

export default function RegisterPage() {
    const router = useRouter()
    const [email, setEmail] = useState('')
    const [password1, setPassword1] = useState('')
    const [password2, setPassword2] = useState('')

    const handleSubmit = async (e) => {
        e.preventDefault()

        if (password1 !== password2) {
            console.error('비밀번호가 일치하지 않습니다')
            return
        }

        try {
            const response = await fetch('http://localhost:8000/api/auth/registration/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    email,
                    password1,
                    password2,
                }),
            })

            if (response.ok) {
                const data = await response.json()
                sessionStorage.setItem('key', data.key)
                console.log('회원가입 성공:', data)
                router.push('/books')
            } else {
                console.error('회원가입 실패')
            }
        } catch (error) {
            console.error('회원가입 에러:', error)
        }
    }

    return (
        <>
            <div className="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
                <div className="sm:mx-auto sm:w-full sm:max-w-sm">
                    <img
                        alt="Your Company"
                        src="https://tailwindui.com/plus/img/logos/mark.svg?color=indigo&shade=600"
                        className="mx-auto h-10 w-auto"
                    />
                    <h2 className="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">
                        회원가입
                    </h2>
                </div>

                <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
                    <form onSubmit={handleSubmit} className="space-y-6">
                        <div>
                            <label htmlFor="email" className="block text-sm/6 font-medium text-gray-900">
                                이메일 주소
                            </label>
                            <div className="mt-2">
                                <input
                                    id="email"
                                    name="email"
                                    type="email"
                                    required
                                    autoComplete="email"
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                    className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                                />
                            </div>
                        </div>

                        <div>
                            <label htmlFor="password1" className="block text-sm/6 font-medium text-gray-900">
                                비밀번호
                            </label>
                            <div className="mt-2">
                                <input
                                    id="password1"
                                    name="password1"
                                    type="password"
                                    required
                                    value={password1}
                                    onChange={(e) => setPassword1(e.target.value)}
                                    className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                                />
                            </div>
                        </div>

                        <div>
                            <label htmlFor="password2" className="block text-sm/6 font-medium text-gray-900">
                                비밀번호 확인
                            </label>
                            <div className="mt-2">
                                <input
                                    id="password2"
                                    name="password2"
                                    type="password"
                                    required
                                    value={password2}
                                    onChange={(e) => setPassword2(e.target.value)}
                                    className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                                />
                            </div>
                        </div>

                        <div>
                            <button
                                type="submit"
                                className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                            >
                                회원가입
                            </button>
                        </div>
                    </form>

                    <p className="mt-10 text-center text-sm/6 text-gray-500">
                        이미 계정이 있으신가요?{' '}
                        <a href="/account/login" className="font-semibold text-indigo-600 hover:text-indigo-500">
                            로그인하기
                        </a>
                    </p>
                </div>
            </div>
        </>
    )
}
