#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-cellranger
Version  : 1.1.0
Release  : 1
URL      : https://cran.r-project.org/src/contrib/cellranger_1.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cellranger_1.1.0.tar.gz
Summary  : Translate Spreadsheet Cell Ranges to Rows and Columns
Group    : Development/Tools
License  : MIT
Requires: R-markdown
Requires: R-rematch
Requires: R-tibble
BuildRequires : R-markdown
BuildRequires : R-rematch
BuildRequires : R-tibble
BuildRequires : clr-R-helpers

%description
of cell range specification.

%prep
%setup -q -c -n cellranger

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521249954

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521249954
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cellranger
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cellranger
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cellranger
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library cellranger|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/cellranger/DESCRIPTION
/usr/lib64/R/library/cellranger/INDEX
/usr/lib64/R/library/cellranger/LICENSE
/usr/lib64/R/library/cellranger/Meta/Rd.rds
/usr/lib64/R/library/cellranger/Meta/features.rds
/usr/lib64/R/library/cellranger/Meta/hsearch.rds
/usr/lib64/R/library/cellranger/Meta/links.rds
/usr/lib64/R/library/cellranger/Meta/nsInfo.rds
/usr/lib64/R/library/cellranger/Meta/package.rds
/usr/lib64/R/library/cellranger/Meta/vignette.rds
/usr/lib64/R/library/cellranger/NAMESPACE
/usr/lib64/R/library/cellranger/NEWS.md
/usr/lib64/R/library/cellranger/R/cellranger
/usr/lib64/R/library/cellranger/R/cellranger.rdb
/usr/lib64/R/library/cellranger/R/cellranger.rdx
/usr/lib64/R/library/cellranger/doc/cell-references.Rmd
/usr/lib64/R/library/cellranger/doc/cell-references.html
/usr/lib64/R/library/cellranger/doc/index.html
/usr/lib64/R/library/cellranger/help/AnIndex
/usr/lib64/R/library/cellranger/help/aliases.rds
/usr/lib64/R/library/cellranger/help/cellranger.rdb
/usr/lib64/R/library/cellranger/help/cellranger.rdx
/usr/lib64/R/library/cellranger/help/paths.rds
/usr/lib64/R/library/cellranger/html/00Index.html
/usr/lib64/R/library/cellranger/html/R.css
