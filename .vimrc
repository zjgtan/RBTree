set nu
syntax on
set ts=4
set autoindent
set expandtab
set shiftwidth=4
set laststatus=1

set fencs=utf-8,GB18030,ucs-bom,default,latin1

"taglist
let Tlist_Show_One_File=1
let Tlist_Exit_OnlyWindow=1
let Tlist_Use_Right_Window=1
let Tlist_Ctags_Cmd="/usr/local/Cellar/ctags/5.8/bin/ctags"
let Tlist_Ctags_Cmd="/usr/local/bin/ptags.py"
let Tlist_Auto_Open=0

map <silent>tl :TlistToggle<CR>

let g:netrw_winsize = 30
nmap <silent>fe :Sexplore!<cr> 

"自动完成括号可引号
""inoremap ( ()<Esc>i
""inoremap [ []<Esc>i
""inoremap { {}<Esc>i
""inoremap ' ''<Esc>i

inoremap jj <ESC>

filetype plugin on

let g:pydiction_location="~/.vim/tools/complete-dict"
let g:pydiction_menu_height=3

"let g:winManagerWindowLayout="FileExplorer"
let g:winManagerWindowLayout='FileExplorer||TagList'
nmap wm :WMToggle<cr>

nmap tg :TagbarToggle<CR>

map <c-j> <c-w>j
map <c-k> <c-w>k
map <c-l> <c-w>l
map <c-h> <c-w>h

set foldmethod=indent

filetype plugin on
set shellslash
set grepprg=grep\ -nH\ $*
filetype indent on
let g:tex_flavor='latex'

"编辑整体配色，目前是最舒服的一个
let colors_name="desert"
hi Normal guifg=#c0c0c0 guibg=#294d4a ctermfg=gray ctermbg=black
hi Pmenu guibg=#444444
hi PmenuSel ctermfg=7 ctermbg=4 guibg=#555555 guifg=#ffffff
" Matched brackets
hi MatchParen ctermfg=7 ctermbg=4 

autocmd BufNewFile *.md 0r ~/.vim/template/md.tlp

set ts=4 sw=4 et
let g:indent_guides_start_level=2
let g:indent_guides_guide_size=1


"pymode
let g:pymode=0
let g:pymode_warnings=0
let g:pymode_paths=[]
let g:pymode_trim_whitespaces=1
let g:pymode_options=1
let g:pymode_doc=0
let g:pep8_ignore="all"
set previewheight=1

filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'
call vundle#end()
filetype plugin indent on

Bundle 'davidhalter/jedi-vim'
