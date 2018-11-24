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
    period: 5
  };

  handleDrawerOpen = () => {
    this.setState({open: true});
  };

  handleDrawerClose = () => {
    this.setState({open: false});
  };

  handleChange = (event, checked) => {
    this.setState({dynamic: checked});
  };

  handleChangePriod = (event) => {
    this.setState({period: event.target.value > 3 || !event.target.value ? event.target.value : 3});
  };

  handleClick = () => {
    this.setState(() => {
    });
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
                Do Register
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
              <Grid item xs={8}>
                <Typography variant="h4" gutterBottom component="h2">
                  Registered Urls
                </Typography>
              </Grid>
              <Grid item xs={2}>
                <TextField
                  id="check-interval"
                  label="Check Interval, sec"
                  type="number"
                  disabled={this.state.dynamic}
                  onChange={this.handleChangePriod}
                  value={this.state.period}
                  className={classes.textField}
                  InputLabelProps={{
                    shrink: true,
                  }}
                />
              </Grid>
              <Grid item xs={2}>
                <FormGroup row>
                  <FormControlLabel
                    control={
                      <Switch
                        checked={this.state.dynamic}
                        onChange={this.handleChange}
                        value="dynamic"
                        color="primary"
                      />
                    }
                    label={this.state.dynamic ? 'Dynamic' : 'Static'}
                  />
                </FormGroup>
              </Grid>
            </Grid>
            <div className={classes.tableContainer}>
              <DataProvider endpoint="api/addresses"
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