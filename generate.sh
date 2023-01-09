
GENERATOR=../src/generator/compile.py
TEMPLATE_DIR=../src

if [ -f README ]; then
    echo "I don't think you want to run this from the root"
    exit 1
fi

rm -r *

cp -r ../static/* .

mkdir -p article

function generate_template {
  echo "python $GENERATOR --template $TEMPLATE_DIR/$1.tmpl"
  python $GENERATOR --template $TEMPLATE_DIR/$1.tmpl --out $2
}

function generate_article {
  echo "python $GENERATOR --article $1 --template $TEMPLATE_DIR/$2.tmpl"
  python $GENERATOR --article $1 --template $TEMPLATE_DIR/$2.tmpl --out $3
}

function md_to_html {
  echo "pandoc -o $2 $1"
  pandoc -o $2 $1
}

generate_template "about.html" "about.html"
generate_template "catshrine.html" "catshrine.html"
generate_template "index.html" "index.html"
generate_template "mods.html" "mods.html"
generate_template "not_found.html" "not_found.html"
generate_template "writings.html" "writings.html"

#for dir in $(cd $TEMPLATE_DIR/articles/ && echo */) ; do
#  dirname=${dir::-1}
#  mkdir -p article/$dirname
#  generate_template articles/$dirname/content.html article/$dirname/main.html
#done


