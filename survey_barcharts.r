# Samuel Crane
# http://www.samuelcrane.com
# https://github.com/samuelcrane
#
# R code
# Make horizontal bar charts with ggplot2 for each Coursera survey response.
# Does not handle text responses.
# See example input file 'survey_response_table.csv'

library('ggplot2')
library('RColorBrewer')

# Label functions from https://github.com/hadley/ggplot2/wiki/labeller
# label_wrap sets the width at a fixed character count
# example call: facet_grid(drv ~ cyl, labeller=label_wrap)
label_wrap <- function(variable, value) {
  lapply(strwrap(as.character(value), width=90, simplify=FALSE), 
         paste, collapse="\n")
}  

# label_wrap_gen allows the width to be set as a parameter of the function call
# example call: facet_grid(~ drv + cyl, labeller=label_wrap_gen(width=15))
label_wrap_gen <- function(width = 25) {
  function(variable, value) {
    lapply(strwrap(as.character(value), width=width, simplify=FALSE), 
           paste, collapse="\n")
  }
}

makeBarchart <- function(x){
  barchart <- ggplot(x, aes(x=reorder(option_text, responses), y=responses, fill=question_text)) 
  barchart <- barchart + geom_bar(width=.75, stat="identity")
  barchart <- barchart + scale_fill_brewer(palette="Set3", guide=FALSE)
  barchart <- barchart + facet_grid(. ~ question_text, labeller=label_wrap)
  barchart <- barchart + coord_flip()
  barchart <- barchart + labs(title = "", x = "", y = "") 
  barchart <- barchart + theme(panel.grid.minor.y = element_blank(), panel.grid.major.y = element_blank())
  barchart
} 

surveyResp <- read.csv('survey_response_table.csv')

by(surveyResp,surveyResp$question_text,
   function(x)
     makeBarchart(x)
)


