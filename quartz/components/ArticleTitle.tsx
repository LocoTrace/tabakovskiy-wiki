import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

const ArticleTitle: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
  const title = fileData.frontmatter?.title

  const slug = fileData.slug ?? ""
  const isIndex = slug === "index" || slug.endsWith("/index")
  if (title && title !== "index") {
    
    return <h1 class={classNames(displayClass, "article-title")}>{title}</h1>
  }

  return null
}

ArticleTitle.css = `
.article-title {
  margin: 2rem 0 0 0;
}
`

export default (() => ArticleTitle) satisfies QuartzComponentConstructor
