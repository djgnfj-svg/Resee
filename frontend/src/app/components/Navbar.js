import Link from 'next/link';

const Navbar = () => {
  return (
    <nav style={{ padding: '10px', background: '#0070f3', color: '#fff' }}>
      <Link href="/" style={{ marginRight: '15px', color: '#fff' }}>
        Home
      </Link>
      <Link href="/custom_user" style={{ marginRight: '15px', color: '#fff' }}>
        Users
      </Link>
      <Link href="/books" style={{ marginRight: '15px', color: '#fff' }}>
        Books
      </Link>
      <Link href="/pots" style={{ color: '#fff' }}>
        Pots
      </Link>
    </nav>
  );
};

export default Navbar;
