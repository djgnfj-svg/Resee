"use client"; // 클라이언트 컴포넌트 선언

import { useEffect, useState } from 'react';
import api from '../utils/api'; // Axios 인스턴스
import Link from 'next/link';

const PotsPage = () => {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchPosts = async () => {
            try {
                const response = await api.get('pots/posts/'); // Django API의 엔드포인트
                setPosts(response.data);
            } catch (error) {
                console.error('Error fetching posts:', error);
            } finally {
                setLoading(false);
            }
        };
        fetchPosts();
    }, []);

    if (loading) return <p>Loading...</p>;

    return (
        <div>
            <h1>Posts</h1>
            <ul>
                {posts.map((post) => (
                    <li key={post.id}>
                        <strong>{post.title}</strong>: {post.script}
                    </li>
                ))}
            </ul>
            <Link href="/">Go back to Home</Link>
        </div>
    );
};

export default PotsPage;
