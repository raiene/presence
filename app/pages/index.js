import Head from './head'
import Content from './content'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import clientPromise from '../lib/mongodb'

export default function Home({ isConnected }) {
  return (
    <div className={styles.container}>
      <Head></Head>
        {isConnected ? (
          <a />
        ) : (
          <h2 className="subtitle">
            You are NOT connected to MongoDB. Check the <code>README.md</code>{' '}
            for instructions.
          </h2>
        )}
      <Content></Content>
      <footer className={styles.footer}>
        
          Powered by{' '}
          <span className={styles.logo}>
            {'r a i e p s '}
          </span>
      </footer>
    </div>
  )
}

export async function getServerSideProps(context) {
  const client = await clientPromise

  // client.db() will be the default database passed in the MONGODB_URI
  // You can change the database by calling the client.db() function and specifying a database like:
  // const db = client.db("myDatabase");
  // Then you can execute queries against your database like so:
  // db.find({}) or any of the MongoDB Node Driver commands

  const isConnected = await client.isConnected()

  return {
    props: { isConnected },
  }
}