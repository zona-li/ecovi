const gulp = require('gulp'), sass = require('gulp-sass');

gulp.task('styles', ()=> {
	return gulp.src('sass/styles.scss')
	.pipe(sass())
	.pipe(gulp.dest('./css'));
});