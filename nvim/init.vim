set number
set linebreak
set wrap
set showbreak=+++
set textwidth=100
set showmatch

set hlsearch
set smartcase
set ignorecase
set incsearch
set autoindent
set expandtab
set shiftwidth=4
set smartindent
set smarttab
set softtabstop=4
set nocompatible
set tabstop=4

set completeopt=noinsert,menuone,noselect
set wildmenu

set ruler
set relativenumber

set scrolloff=5


filetype plugin indent on
syntax on
set clipboard=unnamedplus
filetype plugin on
set cursorline
set ttyfast
set noswapfile

set laststatus=0

set t_Co=256

" Plugins
call plug#begin()

    " Appearance
    Plug 'ryanoasis/vim-devicons'
    
    " Autocompletion
    " Plug 'neoclide/coc.nvim', {'branch': 'release'}
    Plug 'nvim-lua/completion-nvim'
    
    " Utilities
    Plug 'sheerun/vim-polyglot'
    Plug 'ap/vim-css-color'
    Plug 'preservim/nerdtree'

    " Git
    Plug 'airblade/vim-gitgutter'


call plug#end()

" Autocompletion
packadd coc.nvim

function! s:check_back_space() abort
    let col = col('.') - 1
    return !col || getline('.')[col - 1]  =~ '\s'
endfunction

" Insert <tab> when previous text is space, refresh completion if not.
inoremap <silent><expr> <TAB>
    \ coc#pum#visible() ? coc#pum#next(1):
    \ <SID>check_back_space() ? "\<Tab>" :
    \ coc#refresh()
inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : "\<C-h>"
