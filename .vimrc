set nocompatible
set paste! "붙여넣기 계단현상 제거
set title "타이틀바에 현재 편집중인 파일 표시
set ignorecase "찾기에서 대소문자 구별 하지 않음
set nomodeline
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim' "required
Plugin 'nanotech/jellybeans.vim'
Plugin 'majutsushi/tagbar'
Plugin 'scrooloose/nerdtree'
Plugin 'scrooloose/syntastic'
Plugin 'scrooloose/nerdcommenter'
Plugin 'mattn/emmet-vim'
Plugin 'Shougo/neocomplcache.vim'
Plugin 'nathanaelkane/vim-indent-guides'
Plugin 'tpope/vim-fugitive' "repuired
call vundle#end()
filetype plugin indent on

nmap <F8> : Tagbar<CR>
syntax enable # syntax highlighting
set nomodeline
set nu " add line numbers
set smartindent " make smart indent
set tabstop=4 " tab width as 4 (default 8)
set shiftwidth=4
set autoindent "자동 들여쓰기
set ruler "우측하단에 줄,칸 표시
set expandtab
let g:indent_guides_enable_on_vim_startup=1
let g:indent_guides_start_level=2
let g:indent_guides_guide_size=1
let g:tagbar_width=25
let g:NERDTreeWinSize=20
"TAB SIZE 설정
set ts=4 sw=4 et
colorscheme jellybeans

au VimEnter * NERDTreeToggle
au VimEnter * TagbarToggle
