import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

const ArticleTitle: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
  const title = fileData.frontmatter?.title
  const isIndex = fileData.slug && fileData.slug.endsWith("/index")
  // DEBUG: выводим значения для отладки
  console.log('DEBUG ArticleTitle:', {slug: fileData.slug, title, firstHeading: fileData.firstHeading});
  if (title && !(isIndex && title === 'index')) {
    return <h1 class={classNames(displayClass, "article-title")}>{title}</h1>
  } else if (isIndex && fileData.firstHeading) {
    return <h1 class={classNames(displayClass, "article-title")}>{fileData.firstHeading}</h1>
  } else {
    return null;
  }
}

ArticleTitle.css = `
.article-title {
  margin: 2rem 0 0 0;
}
`

export default (() => ArticleTitle) satisfies QuartzComponentConstructor
