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
  page-margin: (left: 4mm, right: 4mm, top: 12mm, bottom: 12mm),
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

        set text(font: font-song, 10pt, baseline: 8pt, spacing: 3pt)

        grid(
          columns: (1fr, 1fr, 1fr),
          align(left, course),
          [] /* align(center, title)*/,
          align(right, date),
        )

        line(length: 100%, stroke: 0.5pt)
      })
    },
  )


  // 页脚
  set page(
    footer: {
      set text(font: font-song, 10pt, baseline: 8pt, spacing: 3pt)
      set align(center)

      grid(
        columns: (1fr, 1fr),
        align(left, authors.map(a => a.name).join(", ")), align(right, counter(page).display("1/1", both: true)),
      )
    },
  )

  set text(font: font-song, lang: "en", size: 11pt)
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
    spacing: 0.75em,
    justify: true,
    first-line-indent: indent,
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

#let statement = it => par(strong(it))

#let options = (..cells) => block(
  width: 100%,
  breakable: true,
  grid(
    row-gutter: 0.6em,
    columns: (1.5em, 1fr),
    ..cells,
  ),
)

#let correct-option = it => {
  underline(
    evade: false,
    offset: 0.2em,
    strong(it),
  )
}

#let explaination = it => block(
  stroke: 0.5pt + black,
  radius: 0.25em,
  inset: 0.5em,
  breakable: true,
  {
    set text(size: 0.8em)
    it
  },
)
