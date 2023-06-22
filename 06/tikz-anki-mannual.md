# tikz anki mannual

## tikz basic drawing 2 lines
\documentclass{article}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
\draw[gray, thick] (-1,2) -- (2,-4);
\draw[gray, thick] (-1,-1) -- (2,2);
\filldraw[black] (0,0) circle (2pt) node[anchor=west]{Intersection point};
\end{tikzpicture}
\end{document}

## tikz draw bezier curve
\documentclass{article}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}

\draw (-2,0) -- (2,0);
\filldraw [gray] (0,0) circle (2pt);
\draw (-2,-2) .. controls (0,0) .. (2,-2);
\draw (-2,2) .. controls (-1,0) and (1,0) .. (2,2);

\end{tikzpicture}
\end{document}

## tikz draw with filled color, 60% red
\documentclass{article}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
\filldraw[color=red!60, fill=red!5, very thick](-1,0) circle (1.5);
\fill[blue!50] (2.5,0) ellipse (1.5 and 0.5);
\draw[ultra thick, ->] (6.5,0) arc (0:220:1);
\end{tikzpicture}
\end{document}

## tikz draw with auto close polygon
\documentclass{article}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
\draw[blue, very thick] (0,0) rectangle (3,2);
\draw[orange, ultra thick] (4,0) -- (6,0) -- (5.7,2) -- cycle;
\end{tikzpicture}
\end{document}

## tikz draw diagrams, how to draw named nodes?
\documentclass{article}
\usepackage{tikz}
\usetikzlibrary{positioning}
\begin{document}
\begin{tikzpicture}[
roundnode/.style={circle, draw=green!60, fill=green!5, very thick, minimum size=7mm},
squarednode/.style={rectangle, draw=red!60, fill=red!5, very thick, minimum size=5mm},
]
%Nodes
\node[squarednode]      (maintopic)                              {2};
\node[roundnode]        (uppercircle)       [above=of maintopic] {1};
\node[squarednode]      (rightsquare)       [right=of maintopic] {3};
\node[roundnode]        (lowercircle)       [below=of maintopic] {4};

%Lines
\draw[->] (uppercircle.south) -- (maintopic.north);
\draw[->] (maintopic.east) -- (rightsquare.west);
\draw[->] (rightsquare.south) .. controls +(down:7mm) and +(right:7mm) .. (lowercircle.east);
\end{tikzpicture}
\end{document}

## tikz style thick values:
ultra thin, very thin, thin, thick, very thick, ultra thick

## tikz style color default values:
white, black, red, green, blue, cyan, magenta, yellow

## tikz how to set rounded corners in node attribute?
\node[squarednode, rounded corners=2mm]      (rightsquare)       [right=of maintopic] {3};


## tikz how to set fill color in style?

{\draw [very thick, draw=gray, fill=white, xshift=\x cm]  (0,5) circle [radius = 0.5cm];


## tikz how to use foreach?
If you provide two numbers before the ..., the \foreach statement will use their difference for the stepping:

\foreach \x in {0, -0.5, ..., -2}
  {\draw [very thick, draw=gray, fill=white, xshift=\x cm]  (0,5) circle [radius = 0.5cm];
  \draw [very thick, fill=gray, xshift=\x cm, draw=white] (-1, 3) -- (1, 3) .. controls (1, 3) and (1,4.3) .. (0, 4.3) .. controls (-1, 4.3) and (-1, 3) .. (-1, 3) -- cycle;
}

## tikz how to do transforms (xshift yshift rotate)?
[xshift=2pt]
[xshift=5pt,yshift=5pt]
[rotate=30]

## tikz how to draw circle and ellipses and rectangle and arc?
\draw (0,0) circle [radius=10pt];
\draw (0,0) ellipse [x radius=20pt, y radius=10pt];
\draw (-0.5,-0.5) rectangle (-1,-1);
\draw (3mm,0mm) arc [start angle=0, end angle=30, radius=3mm];
\draw (0,0) arc [start angle=0, end angle=315, x radius=1.75cm, y radius=1cm];

## tikz how to draw grids?
\draw[step=.5cm] (-1.4,-1.4) grid (1.4,1.4);

## tikz how to use clip?
You can use the \clip command to clip all subsequent drawing.
\begin{tikzpicture}[scale=3]
\clip (-0.1,-0.2) rectangle (1.1,0.75); \draw[step=.5cm,gray,very thin] (-1.4,-1.4) grid (1.4,1.4); \draw (-1.5,0) -- (1.5,0);
\draw (0,-1.5) -- (0,1.5);
\draw (0,0) circle [radius=1cm];
\draw (3mm,0mm) arc [start angle=0, end angle=30, radius=3mm];
\end{tikzpicture}
