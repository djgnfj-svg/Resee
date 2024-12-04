"use client"; // 클라이언트 컴포넌트 선언

import { useEffect, useState } from 'react';
import api from '../utils/api'; // Axios 인스턴스
import axios from 'axios';
import Link from 'next/link';

const BookPage = () => {
    const [books, setBooks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [selectedBook, setSelectedBook] = useState(null);
    const [isCreating, setIsCreating] = useState(false);
    const [showModal, setShowModal] = useState(false);

    useEffect(() => {
        const fetchBooks = async () => {
            try {
                // 로컬 스토리지에서 access_token 가져오기
                const token = localStorage.getItem('access_token');

                console.log(token);

                // Axios 요청 설정
                const response = await axios.get('http://127.0.0.1:8000/api/books/', {
                    headers: {
                        Authorization: `Bearer ${token}`, // 토큰 추가
                    },
                });

                setBooks(response.data); // API 응답 데이터 설정
            } catch (error) {
                console.error('Error fetching books:', error);
            } finally {
                setLoading(false); // 로딩 상태 업데이트
            }
        };

        fetchBooks();
    }, []);

    const handleSave = async () => {
        if (isCreating) {
            try {
                await api.post('books/', { title: selectedBook.title, simple_explanation: selectedBook.simple_explanation });
                alert('Book created successfully');
                setShowModal(false);
                setIsCreating(false);
                const response = await api.get('books/');
                setBooks(response.data);
            } catch (error) {
                console.error('Error creating book:', error);
            }
        } else if (selectedBook) {
            try {
                await api.put(`books/${selectedBook.id}/`, { title: selectedBook.title, simple_explanation: selectedBook.simple_explanation });
                alert('Book updated successfully');
                setIsCreating(false);
                setShowModal(false);
                setBooks(books.map(book => book.id === selectedBook.id ? selectedBook : book));
            } catch (error) {
                console.error('Error updating book:', error);
            }
        }
    };

    const handleDelete = async () => {
        if (selectedBook) {
            const confirmDelete = confirm('삭제하시겠습니까?');
            if (confirmDelete) {
                try {
                    await api.delete(`books/${selectedBook.id}/`);
                    alert('Book deleted successfully');
                    setBooks(books.filter((book) => book.id !== selectedBook.id));
                    setShowModal(false);
                } catch (error) {
                    console.error('Error deleting book:', error);
                }
            }
        }
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setSelectedBook({ ...selectedBook, [name]: value });
    };

    if (loading) return <p>Loading...</p>;

    return (
        <div className="mx-auto max-w-7xl px-4 py-16">
            <div className="flex justify-between items-center mb-8">
                <h1 className="text-3xl font-bold">Books</h1>
                <button
                    onClick={() => { setSelectedBook({ title: '', simple_explanation: '' }); setShowModal(true); setIsCreating(true); }}
                    className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
                >
                    CREATE
                </button>
            </div>
            <div className="max-w-2xl mx-auto px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
                <div className="mt-8 grid grid-cols-1 gap-y-12 sm:grid-cols-2 sm:gap-x-6 lg:grid-cols-4 xl:gap-x-8">
                    {books.map((book) => (
                        <div key={book.id}>
                            <div className="relative">
                                <div className="relative h-72 w-full overflow-hidden rounded-lg">
                                    <img alt='Front of zip tote bag with white canvas, black canvas straps and handle, and black zipper pulls.'
                                        src='/book_covers/cover_white.png' className="size-full object-cover" />
                                </div>
                                <div className="relative mt-4">
                                    <h3 className="text-sm font-medium text-gray-900">{book.title}</h3>
                                    <p className="mt-1 text-sm text-gray-500">{book.simple_explanation}</p>
                                </div>
                            </div>
                            <div className="mt-6">
                                <a
                                    className="relative flex items-center justify-center rounded-md border border-transparent bg-gray-100 px-8 py-2 text-sm font-medium text-gray-900 hover:bg-gray-200"
                                >
                                    바로 복습<span className="sr-only">, {book.name}</span>
                                </a>
                            </div>
                            <div className="mt-2">
                                <button
                                    onClick={() => { setSelectedBook(book); setShowModal(true); }}
                                    className="relative flex items-center justify-center rounded-md border border-transparent bg-blue-500 px-4 py-2 text-sm font-medium text-white hover:bg-blue-600"
                                >
                                    수정/삭제
                                </button>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
            <Link href="/">Go back to Home</Link>

            {showModal && selectedBook && (
                <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
                    <div className="bg-white p-6 rounded-md shadow-md">
                        <input
                            type="text"
                            name="title"
                            value={selectedBook.title}
                            onChange={handleChange}
                            className="w-full p-2 mb-4 border border-gray-300 rounded"
                        />
                        <textarea
                            name="simple_explanation"
                            value={selectedBook.simple_explanation}
                            onChange={handleChange}
                            className="w-full p-2 mb-4 border border-gray-300 rounded"
                        />
                        <div className="mt-4 flex space-x-4">
                            <button
                                onClick={handleSave}
                                className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
                            >
                                업데이트
                            </button>
                            <button
                                onClick={handleDelete}
                                className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600"
                            >
                                삭제
                            </button>
                            <button
                                onClick={() => setShowModal(false)}
                                className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600"
                            >
                                취소
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default BookPage;
