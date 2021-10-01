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
        
          Powered by{' '}
          <span className={styles.logo}>
            {'r a e p s '}
          </span>
      </footer>
    </div>
  )
}
