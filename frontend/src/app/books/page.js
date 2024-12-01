"use client"; // 클라이언트 컴포넌트 선언

import { useEffect, useState } from 'react';
import api from '../utils/api'; // Axios 인스턴스
import Link from 'next/link';

const BookPage = () => {
    const [books, setBooks] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchBooks = async () => {
            try {
                const response = await api.get('books/'); // Django API의 엔드포인트
                setBooks(response.data);
            } catch (error) {
                console.error('Error fetching books:', error);
            } finally {
                setLoading(false);
            }
        };
        fetchBooks();
    }, []);

    if (loading) return <p>Loading...</p>;

    return (
        <div>
            <h1>Books</h1>
            <ul>
                {books.map((book) => (
                    <li key={book.id}>
                        <strong>{book.title}</strong> - {book.simple_explanation}
                    </li>
                ))}
            </ul>
            <Link href="/">Go back to Home</Link>
        </div>
    );
};

export default BookPage;
