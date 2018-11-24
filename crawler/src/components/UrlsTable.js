import React from 'react';
import PropTypes from 'prop-types';
import {withStyles} from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const styles = {
  root: {
    width: '100%',
    overflowX: 'auto',
  },
  table: {
    minWidth: 700,
  },
  bad: {
    color: '#F44336',
  },
  good: {
    color: '#009688'
  }
};


function UrlsTable(props) {
  const {classes, data} = props;

  return (
    <Paper className={classes.root}>
      <Table className={classes.table}>
        <TableHead>
          <TableRow>
            <TableCell>Name</TableCell>
            <TableCell>Url Address</TableCell>
            <TableCell numeric>Status</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map(n => {
            return (
              <TableRow key={n.id}>
                <TableCell component="th" scope="row">
                  {n.name}
                </TableCell>
                <TableCell>
                  <a href={n.urlAddress} target="_blank">{n.urlAddress}</a>
                </TableCell>
                <TableCell numeric className={n.status === 200 ? classes.good : classes.bad}>{n.status}</TableCell>
              </TableRow>
            );
          })}
        </TableBody>
      </Table>
    </Paper>
  );
}

UrlsTable.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(UrlsTable);