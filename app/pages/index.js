import Head from './head'
import Content from './content'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
//import indexpy from '../../pyapp/templates/index.html'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head></Head>
      <Content></Content>
      <footer className={styles.footer}>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{' '}
          <span className={styles.logo}>
            <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16} />
          </span>
        </a>
      </footer>
    </div>
  )
}
