# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xifthen
# catalog-date 2009-05-03 12:26:51 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-xifthen
Version:	1.3
Release:	8
Summary:	Extended conditional commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xifthen
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xifthen.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xifthen.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package extends the ifthen package by implementing new
commands to go within the first argument of \ifthenelse: to
test whether a string is void or not, if a command is defined
or equivalent to another. The package also enables use of
complex expressions as introduced by the package calc, together
with the ability of defining new commands to handle complex
tests. The package requires e-TeX features.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xifthen/xifthen.sty
%doc %{_texmfdistdir}/doc/latex/xifthen/README
%doc %{_texmfdistdir}/doc/latex/xifthen/xifthen.pdf
%doc %{_texmfdistdir}/doc/latex/xifthen/xifthen.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 757658
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 719939
- texlive-xifthen
- texlive-xifthen
- texlive-xifthen

