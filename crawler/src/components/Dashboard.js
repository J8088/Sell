import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import {withStyles} from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import GridList from '@material-ui/core/GridList';
import ListSubheader from '@material-ui/core/ListSubheader';
import GridListTile from '@material-ui/core/GridListTile';
import {mainListItems, secondaryListItems} from './listItems';
import UrlsTable from './UrlsTable';
import Grid from '@material-ui/core/Grid';
import FormGroup from '@material-ui/core/FormGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Switch from '@material-ui/core/Switch';
import DataProvider from "./DataProvider"
import styles from "./DashboardStyles";


class Dashboard extends React.Component {
  state = {
    dynamic: false,
    open: true,
    // crawlUrl: 'http://quotes.toscrape.com/',
    crawlUrl: 'the crawl url',
    crawlerEndpoint: "api/crawl/"
  };

  runCrawler = (url) => {
    const formData = new FormData();
    formData.append('url', url);

    return fetch(
      this.state.crawlerEndpoint, {
        method: 'POST',
        body: formData
      }
    ).then(response => {
      if (response.status !== 200) {
        return this.setState({placeholder: "Something went wrong"});
      }

      return response.json();
    })
      .then(data => {
        if (data.error) {
          return this.setState({placeholder: data.error});
        }
        this.setState({data: data, loaded: true});
      });
  };

  handleDrawerOpen = () => {
    this.setState({open: true});
  };

  handleDrawerClose = () => {
    this.setState({open: false});
  };

  handleStartCrawler = () => {
    console.log(this.state.crawlUrl);
    this.runCrawler(this.state.crawlUrl);
  };

  handleChangeUrl = (event) => {
    this.setState({crawlUrl: event.target.value});
  };


  render() {
    const {classes} = this.props;

    return (
      <React.Fragment>
        <CssBaseline/>
        <div className={classes.root}>
          <AppBar
            position="absolute"
            className={classNames(classes.appBar, this.state.open && classes.appBarShift)}
          >
            <Toolbar disableGutters={!this.state.open} className={classes.toolbar}>
              <IconButton
                color="inherit"
                aria-label="Open drawer"
                onClick={this.handleDrawerOpen}
                className={classNames(
                  classes.menuButton,
                  this.state.open && classes.menuButtonHidden,
                )}
              >
                <MenuIcon/>
              </IconButton>
              <Typography
                component="h1"
                variant="h6"
                color="inherit"
                noWrap
                className={classes.title}
              >
                Crawler
              </Typography>
            </Toolbar>
          </AppBar>
          <Drawer
            variant="permanent"
            classes={{
              paper: classNames(classes.drawerPaper, !this.state.open && classes.drawerPaperClose),
            }}
            open={this.state.open}
          >
            <div className={classes.toolbarIcon}>
              <IconButton onClick={this.handleDrawerClose}>
                <ChevronLeftIcon/>
              </IconButton>
            </div>
            <Divider/>
            <List>{mainListItems}</List>
          </Drawer>
          <main className={classes.content}>
            <div className={classes.appBarSpacer}/>

            <Grid container spacing={24}>
              <Grid item xs={12} sm={10}>
                <TextField
                  required
                  id="url"
                  name="url"
                  label="Url"
                  value={this.state.crawlUrl}
                  onChange={this.handleChangeUrl}
                  fullWidth
                  autoComplete="fname"
                />
              </Grid>
              <Grid item xs={12} sm={1}>
                <Button variant="contained" color="primary"
                        onClick={this.handleStartCrawler}
                        className={classes.button}>
                  Start
                </Button>
              </Grid>
              <Grid item xs={12} sm={1}>
                <Button variant="contained" color="primary"
                        className={classes.button}>
                  Save
                </Button>
              </Grid>
            </Grid>

            <div className={classes.tableContainer}>
              <DataProvider endpoint="api/crawl"
                            dynamic={this.state.dynamic}
                            period={this.state.period}
                            render={data => <UrlsTable data={data}/>}/>
            </div>
          </main>
        </div>
      </React.Fragment>
    );
  }
}

Dashboard.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Dashboard);