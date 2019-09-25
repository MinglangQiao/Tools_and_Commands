### Content

### latex表格相关
2019.09.27 

在线latex表格生成工具： [Tables Generater](https://www.tablesgenerator.com/)

表格1：需要生成一个跨列的表格，但是表格字体会大于正文字体。当表格存在某一行每列都正常时，字体没问题。一旦原始表格的所有行都被合并时，字体就会变大，而且使用\small也没有效果

比如这样,这个勉强还能保持字体：
```latex
\begin{table}
	\centering
	\caption{The training settings for our MT-DNN model.}
%	\vspace{-1em}
	\resizebox{0.5 \textwidth}{!}{
	\begin{tabular}{|c|cc|c|c|}
		\hline
		\multirow{2}{*}{Multi-Row} &
		\multicolumn{3}{c|}{Multi-Column} & 1e-6 \\
		\cline{2-5}
		& column-1 & column-2 & \multicolumn{2}{c|}{w} \\
		\hline
		label-1 & label-2 & label-3 & label-4 & label-5 \\
		\hline
	\end{tabular}}
\label{training settings}
\vspace{-1em}
\end{table}
```
效果是这样的：

![正常字体表格](./latex_gram_img/latex_table_font_normal.jpg)

然后合并一下，这样
```
\begin{table}
	\centering
	\caption{The training settings for our MT-DNN model.}
%	\vspace{-1em}
	\resizebox{0.5 \textwidth}{!}{
	\begin{tabular}{|c|cc|c|c|}
		
		\hline
		\multirow{2}{*}{tes1} &
		\multicolumn{3}{c|}{tes2} & 1e-6 \\
		\cline{2-5}
		& \multicolumn{3}{c|}{w} & column-1  \\
		\hline
		label-1 & label-2 & label-3 & label-4 & label-5 \\
		\hline
	\end{tabular}}
\label{training settings}
\vspace{-1em}
\end{table}
```
现在字体还是正常的，效果是这样的：

![正常字体表格1](./latex_gram_img/latex_table_font_normal1.jpg)

然后再改一下，就不正常了
```
\begin{table}
	\centering
	\caption{The training settings for our MT-DNN model.}
%	\vspace{-1em}
	\resizebox{0.5 \textwidth}{!}{
	\begin{tabular}{|c|cc|c|c|}
		
		\hline
		\multirow{2}{*}{tes1} &
		\multicolumn{3}{c|}{tes2} & 1e-6 \\
		\cline{2-5}
		& \multicolumn{3}{c|}{w} & column-1  \\
		\hline
		\multirow{2}{*}{tes1} &
		\multicolumn{3}{c|}{tes2} & 1e-6 \\
		\cline{2-5}
		& \multicolumn{3}{c|}{w} & column-1  \\
		\hline
	\end{tabular}}
\label{training settings}
\vspace{-1em}
\end{table}
```
现在字体变大了很多，效果是这样的：

![不正常字体表格](./latex_gram_img/latex_table_font_unnormal.jpg)




