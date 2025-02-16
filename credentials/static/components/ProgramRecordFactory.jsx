// TODO: We should be able to remove this as part of https://github.com/openedx/credentials/issues/1722
import React from 'react';
import ReactDOM from 'react-dom';

import ProgramRecord from './ProgramRecord';

function ProgramRecordFactory(parent, props) {
  const formattedProps = {
    ...props.record,
    isPublic: props.isPublic,
    icons: props.icons,
    uuid: props.uuid,
    helpUrl: props.helpUrl,
    programListUrl: props.programListUrl,
  };

  ReactDOM.render(
    React.createElement(ProgramRecord, { ...formattedProps }, null),
    document.getElementById(parent),
  );
}

export { ProgramRecordFactory }; // eslint-disable-line import/prefer-default-export
