set nocompatible
set nomodeline
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim' "required
Plugin 'nanotech/jellybeans.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'scrooloose/syntastic'
Plugin 'scrooloose/nerdcommenter'
Plugin 'mattn/emmet-vim'
Plugin 'Shougo/neocomplcache.vim'
Plugin 'nathanaelkane/vim-indent-guides'
Plugin 'tpope/vim-fugitive' "repuired
call vundle#end()
filetype plugin indent on

syntax enable # syntax highlighting
set nomodeline
set nu " add line numbers
set smartindent " make smart indent
set tabstop=4 " tab width as 4 (default 8)
set shiftwidth=4
set expandtab
let g:indent_guides_enable_on_vim_startup=1
let g:indent_guides_start_level=2
let g:indent_guides_guide_size=1

"TAB SIZE 설정
set ts=4 sw=4 et
colorscheme jellybeans
