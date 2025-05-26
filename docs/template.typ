#import "@preview/tablex:0.0.8": tablex, colspanx, rowspanx, hlinex, vlinex, cellx

#let font-song = ("New Computer Modern", "Source Han Serif SC", "Simsun", "STSong")
#let font-fangsong = ("FangSong", "STFangSong")
#let font-hei = ("Calibri", "Source Han Sans SC", "Source Han Sans HW SC", "SimHei", "Microsoft YaHei", "STHeiti")
#let font-kai = ("KaiTi_GB2312", "KaiTi", "STKaiti")

#let indent = 0em
#let force-indent = 2em
#let fake-par = [#text()[#v(0pt, weak: true)];#text()[#h(0em)]]

#let project(
  course: "软件工程",
  title: "",
  header-content: "",
  authors: (
    (
      name: "memset0",
      email: "memset0@outlook.com",
      link: "https://mem.ac/",
    ),
  ),
  body,
  date: "2025-05-25",
  semester: "Spring-Summer 2025",
  course-code: "CS3165M",
  course-fullname: "Software Engineering",
  page-margin: (left: 6mm, right: 6mm, top: 12mm, bottom: 4mm),
) = {
  if (course-fullname == "") {
    course-fullname = course
  }

  // 文档基本信息
  set document(author: authors.map(a => a.name), title: title)
  set page(
    paper: "a4",
    // flipped: false,
    flipped: true,
    margin: page-margin,
    numbering: "1",
    number-align: center,
  )

  // 页眉
  set page(
    header: {
      locate(loc => {
        if (counter(page).at(loc).at(0) == 1) {
          return none
        }

        set text(font: font-song, size: 8pt, baseline: 6pt)

        grid(
          columns: (3fr, 1fr),
          align(
            left,
            [
              #header-content
            ],
          ),
          align(
            right,
            [
              第 #counter(page).display("1/1", both: true) 页
            ],
          ),
        )

        line(length: 100%, stroke: 0.5pt)
      })
    },
    footer: none,
  )

  set text(font: font-song, lang: "en", size: 10pt)
  show math.equation: set text(weight: 400)

  // set heading(numbering: "1.1)")

  block(
    stroke: 0.5pt + black,
    radius: 0.25em,
    width: 100%,
    inset: 1em,
    outset: -0.2em,
  )[
    #text(size: 0.8em)[#grid(
        columns: (auto, 1fr, auto),
        align(left, strong(course-code)), [], align(right, strong(course-fullname)),
      )]
    // #v(0.5em)
    #align(center)[#text(size: 1.25em)[#title]]
    // #v(0.5em)
    #block(
      ..authors.map(author => align(center)[
        #text(size: 0.8em)[#grid(
            columns: (auto, 1fr, auto),
            align(
              left,
              {
                author.name
                if "id" in author {
                  " (" + author.id + ")"
                }
              },
            ),
            [],
            align(right, author.email),
          )]
      ]),
    )
  ]

  // Main body.

  show heading: set block(below: 1em)
  set par(
    leading: 0.5em,
    spacing: 0.5em,
    // justify: true,
    first-line-indent: indent,
  )
  set text(
    tracking: -0.0125em,
    cjk-latin-spacing: none,
  )
  show "。": "．"
  show "（": "("
  show "）": ")"

  set table(inset: 5pt, stroke: 0.5pt, align: horizon + center)

  set columns(gutter: 1em)

  show raw.where(block: true): it => {
    set par(justify: false)
    it
  }

  {
    columns(3, gutter: 1em, body)
  }
}

#let _style-stroke = 0.375pt + black
#let _style-stroke-dashed = (paint: black, thickness: 0.375pt, dash: "densely-dashed")
#let _style-inset = 0.3125em

#let statement = it => par(strong(it))

#let options = (..cells) => block(
  width: 100%,
  breakable: true,
  grid(
    row-gutter: 0.5em,
    columns: (1.5em, 1fr),
    ..cells,
  ),
)

#let correct-option = it => {
  underline(
    evade: false,
    offset: 0.15em,
    strong(it),
  )
}

#let explaination = (..it) => block(
  stroke: _style-stroke,
  radius: 0.125em,
  breakable: true,
  clip: true,
  {
    set text(size: 0.6em)
    set par(justify: true)
    table(
      columns: 1fr,
      stroke: _style-stroke-dashed,
      inset: _style-inset,
      align: horizon + left,
      ..it,
    )
    // stack(..(
    //   it
    //     .pos()
    //     .enumerate()
    //     .map(((idx, it)) => {
    //       if idx > 0 {
    //         line(length: 100%, stroke: _style-stroke)
    //       }
    //       block(
    //         spacing: 0em,
    //         inset: _style-inset,
    //         breakable: true,
    //         it,
    //       )
    //     })
    // ))
  },
)

#let spacing = v(0.5em)

#let index = it => {
  h(1fr)
  super(text(weight: "regular")[#it])
}

#let hr = block(line(length: 100% + _style-inset * 2, stroke: _style-stroke))

#let hint = {
  block([
    #set text(weight: "semibold")
    #set par(justify: true)
    本题目集由 \@memset0 制作，如有任何问题欢迎反馈。题目集源自课程组官网例题，翻译和题目解析使用 GPT 4.1 生成，感谢小角龙学长爬取的题目数据。
  ])
  v(1em)
}
